import { Timeline, AppState } from '../models/types.js';

export const goldfishState: AppState = {
    currentChapterIndex: 0,
    currentSectionIndex: 0,
    sectionStartTime: Date.now(),
    isPaused: true,
    pausedAt: Date.now(),
    hasStarted: false,
    sessionEndTime: 0,
    rightPanelMode: 'info',
    pendingMandatoryPrompt: false,
    completedMandatoryPromptKeys: [],
};

interface TimelinePosition {
    chapterIndex: number;
    sectionIndex: number;
}

function flattenPositions(timeline: Timeline): TimelinePosition[] {
    const positions: TimelinePosition[] = [];
    for (let chapterIndex = 0; chapterIndex < timeline.chapters.length; chapterIndex++) {
        const chapter = timeline.chapters[chapterIndex];
        for (let sectionIndex = 0; sectionIndex < chapter.sections.length; sectionIndex++) {
            positions.push({ chapterIndex, sectionIndex });
        }
    }
    return positions;
}

function currentFlatIndex(timeline: Timeline): number {
    const positions = flattenPositions(timeline);
    return positions.findIndex(
        p => p.chapterIndex === goldfishState.currentChapterIndex && p.sectionIndex === goldfishState.currentSectionIndex,
    );
}

function initSessionEndTime(timeline: Timeline): void {
    if (!goldfishState.hasStarted) {
        const totalMs = timeline.chapters
            .flatMap(chapter => chapter.sections)
            .reduce((s, section) => s + section.durationSeconds, 0) * 1000;
        goldfishState.sessionEndTime = Date.now() + totalMs;
    }
}

function isMandatoryPromptSection(timeline: Timeline, position: TimelinePosition): boolean {
    const section = timeline.chapters[position.chapterIndex]?.sections[position.sectionIndex];
    return section?.type === 'Prompt' && section.isMandatory === true;
}

function getPositionKey(position: TimelinePosition): string {
    return `${position.chapterIndex}:${position.sectionIndex}`;
}

function isMandatoryPromptCompleted(position: TimelinePosition): boolean {
    return goldfishState.completedMandatoryPromptKeys.includes(getPositionKey(position));
}

function isCurrentMandatoryPromptPending(timeline: Timeline): boolean {
    const position = {
        chapterIndex: goldfishState.currentChapterIndex,
        sectionIndex: goldfishState.currentSectionIndex,
    };

    return isMandatoryPromptSection(timeline, position) && !isMandatoryPromptCompleted(position);
}

function getPositionIndex(position: TimelinePosition, timeline: Timeline): number {
    const positions = flattenPositions(timeline);
    return positions.findIndex(
        p => p.chapterIndex === position.chapterIndex && p.sectionIndex === position.sectionIndex,
    );
}

function findFirstIncompleteMandatoryPromptBefore(targetPosition: TimelinePosition, timeline: Timeline): TimelinePosition | undefined {
    const positions = flattenPositions(timeline);
    const currentIndex = currentFlatIndex(timeline);
    const targetIndex = getPositionIndex(targetPosition, timeline);

    if (currentIndex < 0 || targetIndex <= currentIndex) {
        return undefined;
    }

    for (let index = currentIndex + 1; index <= targetIndex; index++) {
        const position = positions[index];
        if (isMandatoryPromptSection(timeline, position) && !isMandatoryPromptCompleted(position)) {
            return position;
        }
    }

    return undefined;
}

function resolveTargetPosition(targetPosition: TimelinePosition, timeline: Timeline): TimelinePosition {
    return findFirstIncompleteMandatoryPromptBefore(targetPosition, timeline) ?? targetPosition;
}

function canMoveToPosition(position: TimelinePosition, timeline: Timeline): boolean {
    if (!isCurrentMandatoryPromptPending(timeline)) {
        return true;
    }

    return position.chapterIndex === goldfishState.currentChapterIndex
        && position.sectionIndex === goldfishState.currentSectionIndex;
}

function moveToPosition(position: TimelinePosition, timeline: Timeline): void {
    initSessionEndTime(timeline);

    const now = Date.now();
    const requiresAcknowledgement = isMandatoryPromptSection(timeline, position) && !isMandatoryPromptCompleted(position);

    goldfishState.currentChapterIndex = position.chapterIndex;
    goldfishState.currentSectionIndex = position.sectionIndex;
    goldfishState.sectionStartTime = now;
    goldfishState.isPaused = requiresAcknowledgement;
    goldfishState.pausedAt = requiresAcknowledgement ? now : undefined;
    goldfishState.hasStarted = true;
    goldfishState.rightPanelMode = 'info';
    goldfishState.pendingMandatoryPrompt = requiresAcknowledgement;
}

export function navigateToSectionInChapter(sectionIndex: number, timeline: Timeline): void {
    const chapter = timeline.chapters[goldfishState.currentChapterIndex];
    if (sectionIndex < 0 || sectionIndex >= chapter.sections.length) {
        return;
    }

    const requestedPosition = { chapterIndex: goldfishState.currentChapterIndex, sectionIndex };
    const targetPosition = resolveTargetPosition(requestedPosition, timeline);
    if (!canMoveToPosition(targetPosition, timeline)) {
        return;
    }

    moveToPosition(targetPosition, timeline);
}

export function advanceSegment(timeline: Timeline): void {
    const positions = flattenPositions(timeline);
    const current = currentFlatIndex(timeline);
    if (current >= 0 && current < positions.length - 1) {
        const requestedPosition = positions[current + 1];
        const targetPosition = resolveTargetPosition(requestedPosition, timeline);
        if (!canMoveToPosition(targetPosition, timeline)) {
            return;
        }
        moveToPosition(targetPosition, timeline);
    }
}

export function previousSegment(timeline: Timeline): void {
    const positions = flattenPositions(timeline);
    const current = currentFlatIndex(timeline);
    if (current > 0) {
        const targetPosition = positions[current - 1];
        if (!canMoveToPosition(targetPosition, timeline)) {
            return;
        }
        moveToPosition(targetPosition, timeline);
    }
}

export function advanceChapter(timeline: Timeline): void {
    const nextChapterIndex = goldfishState.currentChapterIndex + 1;
    if (nextChapterIndex < timeline.chapters.length) {
        const requestedPosition = { chapterIndex: nextChapterIndex, sectionIndex: 0 };
        const targetPosition = resolveTargetPosition(requestedPosition, timeline);
        if (!canMoveToPosition(targetPosition, timeline)) {
            return;
        }
        moveToPosition(targetPosition, timeline);
    }
}

export function previousChapter(timeline: Timeline): void {
    const prevChapterIndex = goldfishState.currentChapterIndex - 1;
    if (prevChapterIndex >= 0) {
        const targetPosition = { chapterIndex: prevChapterIndex, sectionIndex: 0 };
        if (!canMoveToPosition(targetPosition, timeline)) {
            return;
        }
        moveToPosition(targetPosition, timeline);
    }
}

export function openNotesPanel(): void {
    goldfishState.rightPanelMode = 'notes';
}

export function closeNotesPanel(): void {
    goldfishState.rightPanelMode = 'info';
}

function hasTranscript(section: Timeline['chapters'][number]['sections'][number]): boolean {
    return typeof section.transcript === 'string' && section.transcript.trim().length > 0;
}

export function advanceNotesSection(timeline: Timeline): void {
    const positions = flattenPositions(timeline);
    const current = currentFlatIndex(timeline);
    if (current < 0) {
        return;
    }

    for (let i = current + 1; i < positions.length; i++) {
        const requestedPosition = positions[i];
        const section = timeline.chapters[requestedPosition.chapterIndex].sections[requestedPosition.sectionIndex];
        if (hasTranscript(section)) {
            const targetPosition = resolveTargetPosition(requestedPosition, timeline);
            if (!canMoveToPosition(targetPosition, timeline)) {
                return;
            }
            moveToPosition(targetPosition, timeline);
            goldfishState.rightPanelMode = 'notes';
            return;
        }
    }
}

export function previousNotesSection(timeline: Timeline): void {
    const positions = flattenPositions(timeline);
    const current = currentFlatIndex(timeline);
    if (current <= 0) {
        return;
    }

    for (let i = current - 1; i >= 0; i--) {
        const position = positions[i];
        const section = timeline.chapters[position.chapterIndex].sections[position.sectionIndex];
        if (hasTranscript(section)) {
            if (!canMoveToPosition(position, timeline)) {
                return;
            }
            moveToPosition(position, timeline);
            goldfishState.rightPanelMode = 'notes';
            return;
        }
    }
}

export function markCurrentMandatoryPromptComplete(timeline: Timeline, completed: boolean): void {
    const position = {
        chapterIndex: goldfishState.currentChapterIndex,
        sectionIndex: goldfishState.currentSectionIndex,
    };

    if (!isMandatoryPromptSection(timeline, position)) {
        return;
    }

    const key = getPositionKey(position);
    const existingIndex = goldfishState.completedMandatoryPromptKeys.indexOf(key);

    if (completed) {
        if (existingIndex < 0) {
            goldfishState.completedMandatoryPromptKeys.push(key);
        }
        goldfishState.pendingMandatoryPrompt = false;
        return;
    }

    if (existingIndex >= 0) {
        goldfishState.completedMandatoryPromptKeys.splice(existingIndex, 1);
    }

    goldfishState.pendingMandatoryPrompt = true;
    goldfishState.isPaused = true;
    goldfishState.pausedAt = Date.now();
}

export function pauseResume(timeline?: Timeline): void {
    if (goldfishState.isPaused) {
        const hasIncompleteMandatoryPrompt = timeline
            ? isCurrentMandatoryPromptPending(timeline)
            : goldfishState.pendingMandatoryPrompt;

        if (hasIncompleteMandatoryPrompt) {
            goldfishState.pendingMandatoryPrompt = true;
            return;
        }

        if (!goldfishState.hasStarted) {
            goldfishState.sectionStartTime = Date.now();
            if (timeline) {
                initSessionEndTime(timeline);
            }
        } else {
            const pauseDuration = Date.now() - (goldfishState.pausedAt ?? Date.now());
            goldfishState.sectionStartTime += pauseDuration;
            goldfishState.sessionEndTime += pauseDuration;
        }
        goldfishState.isPaused = false;
        goldfishState.pausedAt = undefined;
        goldfishState.hasStarted = true;
    } else {
        goldfishState.pausedAt = Date.now();
        goldfishState.isPaused = true;
    }
}
