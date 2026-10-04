<script lang="ts">
	import { getFinanceState } from '$lib/stores/finance-store.svelte';

	interface Props {
		filterBy: {
			name: string;
			type: string;
		};
	}

	const financeState = getFinanceState();

	let { filterBy = $bindable() }: Props = $props();
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
			id="account_name"
			type="search"
			placeholder="Search accounts"
			class="w-full rounded-md border border-line bg-page py-2 pr-3 pl-9 text-sm focus:ring-0"
			bind:value={filterBy.name}
		/>
	</label>
	<select
		id="account_type"
		class="min-w-37.5 rounded-md border border-line bg-page px-3 py-2 text-sm capitalize focus:ring-0"
		bind:value={filterBy.type}
	>
		<option value="">All types</option>
		{#each financeState.accountTypes as category}
			<option value={category} class="capitalize">{category.replaceAll('_', ' ')}</option>
		{/each}
	</select>
</div>
