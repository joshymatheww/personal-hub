<script lang="ts">
	import { goto } from '$app/navigation';
	import { fetchResource } from '$lib/apis/http';
	import WorkoutsManagerHeader from '$lib/components/layout/WorkoutsManagerHeader.svelte';
	import { authStore } from '$lib/stores/auth-store.svelte';
	import { getWorkoutState } from '$lib/stores/workouts-store.svelte';
	import type { WorkoutsMetaData } from '$lib/types/workouts';
	import { format } from 'date-fns';
	import { onMount } from 'svelte';

	let { children } = $props();

	const workoutState = getWorkoutState();

	onMount(async () => {
		if (!authStore.token) {
			authStore.logout();
			goto('/');
		} else {
			try {
				const workoutsMetadata = await fetchResource<WorkoutsMetaData>(
					authStore.token,
					'workouts/meta-data'
				);
				workoutState.setWorkoutsMetaData(workoutsMetadata);
			} catch (error) {
				console.log(error);
			}
		}
	});
</script>

<section id="dashboard">
	<div class="mb-1 flex flex-wrap items-baseline justify-between gap-x-6 gap-y-2">
		<h1 class="font-display text-3xl font-bold tracking-tight sm:text-4xl">Workouts Manager</h1>
		<span class="text-sm font-semibold tabular-nums">
			{format(new Date(), 'EEEE, d LLLL')}
		</span>
	</div>
	<WorkoutsManagerHeader />
	{@render children()}
</section>
