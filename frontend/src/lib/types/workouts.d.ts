export type MuscleGroups = string[];
export type Equipements = string[];
export type SplitType = {
	label: string;
	value: string;
};

export interface WorkoutsMetaData {
	equipements: Equipements;
	muscle_groups: MuscleGroups;
	split_types: SplitType[];
}

export interface WorkoutLibraryBase {
	name: string;
	targeted_muscle: string;
	recovery_time_hours?: number;
	valid_splits: string[];
	equipement?: string;
}

export interface WorkoutsLibrary extends WorkoutLibraryBase {
	id: number;
}
