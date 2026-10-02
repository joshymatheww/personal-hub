import { getContext, setContext } from 'svelte';

import type { WorkoutsMetaData } from '$lib/types/workouts';

export class WorkoutStore {
	workoutsMetaData = $state<WorkoutsMetaData | null>(null);

	setWorkoutsMetaData(metaData: WorkoutsMetaData) {
		this.workoutsMetaData = metaData;
	}
}

const WORKOUT_STATE_KEY = Symbol('WORKOUT_STATE');

export function setWorkoutState() {
	return setContext(WORKOUT_STATE_KEY, new WorkoutStore());
}

export function getWorkoutState() {
	return getContext<ReturnType<typeof setWorkoutState>>(WORKOUT_STATE_KEY);
}
