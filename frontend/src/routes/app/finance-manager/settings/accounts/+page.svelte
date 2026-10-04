<script lang="ts">
	import AccountsFilter from '$lib/components/finanace-manager/accounts/AccountsFilter.svelte';
	import AccountsList from '$lib/components/finanace-manager/accounts/AccountsList.svelte';
	import NewAccountForm from '$lib/components/finanace-manager/accounts/NewAccountForm.svelte';

	let filterBy = $state({
		name: '',
		type: ''
	});
</script>

<svelte:head>
	<title>Accounts | Settings | Fianance Manager | Personal Hub</title>
</svelte:head>

<div class="mb-6 flex flex-wrap items-baseline justify-between gap-4">
	<div>
		<h1 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">Accounts</h1>
		<p class="text-muted mt-1">Configure and link your working accounts here...</p>
	</div>
</div>
<div class="grid gap-4 lg:grid-cols-[1fr_360px]">
	<div class="@container">
		<AccountsFilter bind:filterBy />
		<AccountsList bind:filterBy />
	</div>
	<NewAccountForm />
</div>
