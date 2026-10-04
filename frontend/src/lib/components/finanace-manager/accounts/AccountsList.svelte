<script lang="ts">
	import { getFinanceState } from '$lib/stores/finance-store.svelte';

	const financeState = getFinanceState();
	let accountsQuery = financeState.getAllAccounts();
</script>

<div class="grid grid-cols-1 gap-4 @lg:grid-cols-2 @3xl:grid-cols-3">
	{#if accountsQuery.isLoading}
		<div>Loading..</div>
	{:else}
		{#each accountsQuery.data as exercise}
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
				<p class="text-muted mt-1 text-sm">{exercise.balance}</p>
				<div class="mt-3 flex flex-wrap gap-1.5 text-xs">
					<span class="rounded-full bg-ink px-2.5 py-1 font-medium text-panel capitalize">
						{exercise.type.replaceAll('_', ' ')}
					</span>
				</div>
			</article>
		{/each}
	{/if}
</div>
