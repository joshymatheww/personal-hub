<script lang="ts">
	import Input from '$lib/components/form/Input.svelte';
	import { WorkousLibraryForm } from '$lib/models/workouts-library-form.svelte';
	import { getWorkoutState } from '$lib/stores/workouts-store.svelte';

	const form = new WorkousLibraryForm();

	const workoutsState = getWorkoutState();
	const categories = $derived.by(() => {
		return workoutsState.workoutsMetaData?.split_types ?? [];
	});
	const equipements = $derived.by(() => workoutsState.workoutsMetaData?.equipements);
	const muscleGroups = $derived.by(() => workoutsState.workoutsMetaData?.muscle_groups);
</script>

<aside class="h-fit rounded-lg border border-line bg-panel p-5 sm:p-6">
	<h2 class="mb-3 font-semibold">Add an exercise</h2>
	<div>
		<Input
			id="name"
			name="name"
			label="Name"
			placeholder="eg: Cable lateral raise"
			bind:value={form.name}
		/>
	</div>

	<div class="my-3">
		<Input
			id="recovery_time_hours"
			name="recovery_time_hours"
			label="Recovery Time"
			placeholder="eg: Cable lateral raise"
			bind:value={form.recovery_time_hours}
		/>
	</div>

	<div class="mt-4">
		<span class="text-muted text-sm">Required equipement</span>
		<div class="mt-2 flex flex-wrap gap-2">
			{#each equipements as equipement}
				<button
					class="hover:border-muted rounded-full border border-line bg-page px-3 py-1.5 text-xs"
				>
					{equipement}
				</button>
			{/each}
		</div>
	</div>

	<div class="mt-4">
		<span class="text-muted text-sm">Muscle groups it trains</span>
		<div class="mt-2 flex flex-wrap gap-2">
			{#each muscleGroups as muscle}
				<button
					class="hover:border-muted rounded-full border border-line bg-page px-3 py-1.5 text-xs"
				>
					{muscle}
				</button>
			{/each}
		</div>
	</div>

	<div class="mt-4">
		<span class="text-muted text-sm">Categories</span>
		<div class="mt-2 flex flex-wrap gap-2">
			{#each categories as category}
				<button
					class="hover:border-muted rounded-full border border-line bg-page px-3 py-1.5 text-xs"
				>
					{category.label}
				</button>
			{/each}
		</div>
	</div>

	<label class="mt-4 block text-sm">
		<span class="text-muted">Notes</span>
		<textarea
			rows="2"
			class="mt-1 w-full rounded-md border border-line bg-page px-3 py-2"
			placeholder="Cues, form notes…"></textarea>
	</label>

	<button class="mt-5 w-full rounded-md bg-ink px-4 py-2.5 font-medium text-panel"
		>Save exercise</button
	>
</aside>
