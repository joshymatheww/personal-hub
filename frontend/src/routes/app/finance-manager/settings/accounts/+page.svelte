<script lang="ts">
	import AccountsFilter from '$lib/components/finanace-manager/accounts/AccountsFilter.svelte';
	import AccountsList from '$lib/components/finanace-manager/accounts/AccountsList.svelte';
	import NewAccountForm from '$lib/components/finanace-manager/accounts/NewAccountForm.svelte';
	import Plus from '$lib/components/icons/Plus.svelte';
	import Modal from '$lib/components/ui/Modal.svelte';

	let filterBy = $state({
		name: '',
		type: ''
	});

	let isNewAccountModalOpen = $state(false);
</script>

<svelte:head>
	<title>Accounts | Settings | Finance Manager | Personal Hub</title>
</svelte:head>

<div class="mb-6 flex flex-wrap items-baseline justify-between gap-4">
	<div class="w-full">
		<div class="flex items-center justify-between">
			<h1 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">Accounts</h1>
			<button
				onclick={() => (isNewAccountModalOpen = !isNewAccountModalOpen)}
				class="mr-1 flex items-center gap-1.5 rounded-md bg-ink px-4 py-2 text-sm font-medium text-panel hover:bg-ink/90 lg:hidden"
			>
				<Plus />
				<span>New Account</span>
			</button>
		</div>
		<p class="text-muted mt-1">Configure and link your working accounts here...</p>
	</div>
</div>
<div class="grid gap-4 lg:grid-cols-[1fr_380px]">
	<div class="@container">
		<AccountsFilter bind:filterBy />
		<AccountsList bind:filterBy />
	</div>
	<div class="hidden lg:block">
		<NewAccountForm />
	</div>
</div>

<Modal bind:isOpen={isNewAccountModalOpen} title="Create new account">
	<NewAccountForm showTitle={false} onSave={() => (isNewAccountModalOpen = false)} />
</Modal>
