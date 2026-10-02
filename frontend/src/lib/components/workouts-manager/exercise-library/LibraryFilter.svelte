<script lang="ts">
	import { getWorkoutState } from '$lib/stores/workouts-store.svelte';

	const workoutsState = getWorkoutState();
	const categories = $derived.by(() => {
		return workoutsState.workoutsMetaData?.split_types ?? [];
	});
	const muscleGroups = $derived.by(() => {
		if (workoutsState.workoutsMetaData?.muscle_groups) {
			return workoutsState.workoutsMetaData?.muscle_groups.map((g) => {
				return {
					label: g,
					value: g.toLowerCase()
				};
			});
		}
		return [];
	});
</script>

<div class="mb-4 flex flex-wrap items-center gap-3 rounded-lg border border-line bg-panel p-4">
	<label class="relative min-w-50 flex-1">
		<svg
			viewBox="0 0 24 24"
			class="text-muted pointer-events-none absolute top-1/2 left-3 h-4 w-4 -translate-y-1/2"
			fill="none"
			stroke="currentColor"
			stroke-width="1.8"><circle cx="11" cy="11" r="6" /><path d="M20 20l-3.5-3.5" /></svg
		>
		<input
			id="exercise_name"
			type="search"
			placeholder="Search exercises"
			class="w-full rounded-md border border-line bg-page py-2 pr-3 pl-9 text-sm focus:ring-0"
		/>
	</label>
	<select
		id="exercise_split_type"
		class="min-w-37.5 rounded-md border border-line bg-page px-3 py-2 text-sm focus:ring-0"
	>
		<option>All categories</option>
		{#each categories as category}
			<option value={category.value}>{category.label}</option>
		{/each}
	</select>
	<select
		id="muscle_group"
		class="min-w-40 rounded-md border border-line bg-page px-3 py-2 text-sm focus:ring-0"
	>
		<option>All muscle groups</option>
		{#each muscleGroups as group}
			<option value={group.value}>{group.label}</option>
		{/each}
	</select>
</div>
