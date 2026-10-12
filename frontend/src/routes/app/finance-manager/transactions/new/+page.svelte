<!-- src/routes/app/finance/transactions/new/+page.svelte -->
<script lang="ts">
	import NewTransaction from '$lib/components/finanace-manager/transactions/NewTransaction.svelte';
	import { getAccountState } from '$lib/stores/finance-manager/accounts-store.svelte';

	const accountState = getAccountState();

	const metadataQuery = accountState.getMeataData();
	const accountsQuery = accountState.getAllAccounts();
</script>

<svelte:head>
	<title>New Transaction | Fianance Manager | Personal Hub</title>
</svelte:head>

<div class="mx-auto max-w-5xl px-4">
	<div class="mb-6">
		<h1 class="text-2xl font-bold text-ink">New Transaction</h1>
		<p class="text-muted text-sm">Record a new movement in your financial ledger.</p>
	</div>

	{#if metadataQuery.isLoading || accountsQuery.isLoading}
		<div>Loading system schemas...</div>
	{:else if metadataQuery.isError || accountsQuery.isError}
		<div class="text-red-500">Failed to load interface configurations.</div>
	{:else}
		<NewTransaction />
	{/if}
</div>
