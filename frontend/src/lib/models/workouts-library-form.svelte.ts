import { postResource } from '$lib/apis/http';
import type { WorkoutLibraryBase, WorkoutsLibrary } from '$lib/types/workouts';
import { BaseForm } from './base-form.svelte';

export class WorkousLibraryForm extends BaseForm<WorkoutLibraryBase, WorkoutsLibrary> {
	name = $state('');
	targeted_muscle = $state('');
	recovery_time_hours = $state(48);
	valid_splits = $state<string[]>([]);
	equipement = $state('');

	async executeSubmit(token: string): Promise<WorkoutsLibrary> {
		const newExericse: WorkoutLibraryBase = {
			name: this.name,
			targeted_muscle: this.targeted_muscle,
			recovery_time_hours: this.recovery_time_hours,
			valid_splits: this.valid_splits,
			equipement: this.equipement
		};
		const result = await postResource<WorkoutLibraryBase, WorkoutsLibrary>(
			newExericse,
			token,
			'workouts/library'
		);
		return result;
	}
}
