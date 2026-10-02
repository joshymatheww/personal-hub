<script lang="ts">
	import { goto } from '$app/navigation';
	import { fetchResource } from '$lib/apis/http';
	import { authStore } from '$lib/stores/auth-store.svelte';
	import type { WorkoutsLibrary } from '$lib/types/workouts';
	import { onMount } from 'svelte';

	let loading = $state(false);
	let exercises = $state<WorkoutsLibrary[]>([]);

	onMount(async () => {
		if (!authStore.token) {
			authStore.logout();
			goto('/');
		} else {
			try {
				const result = await fetchResource<WorkoutsLibrary[]>(authStore.token, 'workouts/library');
				exercises = result;
			} catch (error) {
				console.log(error);
			}
		}
	});
</script>

<div class="grid gap-4 sm:grid-cols-2">
	{#if loading}
		<div>Loading..</div>
	{:else}
		{#each exercises as exercise}
			<article class="rounded-lg border border-line bg-panel p-5">
				<div class="flex items-start justify-between gap-3">
					<h2 class="font-semibold">{exercise.name}</h2>
					<button
						class="text-muted -mt-1 -mr-2 grid h-8 w-8 shrink-0 place-items-center rounded-md hover:bg-page"
						aria-label="Options"
						><svg viewBox="0 0 24 24" class="h-5 w-5" fill="currentColor"
							><circle cx="12" cy="5" r="1.6" /><circle cx="12" cy="12" r="1.6" /><circle
								cx="12"
								cy="19"
								r="1.6"
							/></svg
						></button
					>
				</div>
				<p class="text-muted mt-1 text-sm">{exercise.equipement}</p>
				<div class="mt-3 flex flex-wrap gap-1.5 text-xs">
					<span class="rounded-full bg-ink px-2.5 py-1 font-medium text-panel"
						>{exercise.valid_splits}</span
					>
					<span class="rounded-full bg-page px-2.5 py-1">Chest</span>
					<span class="rounded-full bg-page px-2.5 py-1">Front delts</span>
					<span class="rounded-full bg-page px-2.5 py-1">Triceps</span>
				</div>
			</article>
		{/each}
	{/if}
</div>
