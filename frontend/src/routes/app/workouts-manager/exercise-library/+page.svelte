<script lang="ts">
	import ExercisesList from '$lib/components/workouts-manager/exercise-library/ExercisesList.svelte';
	import LibraryFilter from '$lib/components/workouts-manager/exercise-library/LibraryFilter.svelte';
	import NewExerciseForm from '$lib/components/workouts-manager/exercise-library/NewExerciseForm.svelte';
</script>

<svelte:head>
	<title>Exercise Library | Workouts Manager | Personal Hub</title>
</svelte:head>

<div class="mb-6 flex flex-wrap items-baseline justify-between gap-4">
	<div>
		<h1 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">Exercise library</h1>
		<p class="text-muted mt-1">— each one links to the muscle groups and categories it trains.</p>
	</div>
</div>
<div class="grid gap-4 lg:grid-cols-[1fr_360px]">
	<div>
		<LibraryFilter />
		<ExercisesList />
	</div>
	<NewExerciseForm />
</div>
