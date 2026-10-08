<script lang="ts">
	import TransactionGroupFilter from '$lib/components/finanace-manager/transaction-group/TransactionGroupFilter.svelte';
	import TransactionGroupList from '$lib/components/finanace-manager/transaction-group/TransactionGroupList.svelte';
	import NewTransactionGroupForm from '$lib/components/finanace-manager/transaction-group/NewTransactionGroupForm.svelte';
	import Plus from '$lib/components/icons/Plus.svelte';
	import Modal from '$lib/components/ui/Modal.svelte';

	let filterBy = $state({
		name: '',
		type: ''
	});

	let isNewGroupModalOpen = $state(false);
</script>

<svelte:head>
	<title>Transaction Group | Settings | Finance Manager | Personal Hub</title>
</svelte:head>

<div class="mb-6 flex flex-wrap items-baseline justify-between gap-4">
	<div class="w-full">
		<div class="flex items-center justify-between">
			<h1 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">Transaction Groups</h1>
			<button
				onclick={() => (isNewGroupModalOpen = !isNewGroupModalOpen)}
				class="mr-1 flex items-center gap-1.5 rounded-md bg-ink px-4 py-2 text-sm font-medium text-panel hover:bg-ink/90 lg:hidden"
			>
				<Plus />
				<span>New Group</span>
			</button>
		</div>
		<p class="text-muted mt-1">Configure tranasction groups here...</p>
	</div>
</div>
<div class="grid gap-4 lg:grid-cols-[1fr_380px]">
	<div class="@container">
		<TransactionGroupFilter bind:filterBy />
		<TransactionGroupList bind:filterBy />
	</div>
	<div class="hidden lg:block">
		<NewTransactionGroupForm />
	</div>
</div>

<Modal bind:isOpen={isNewGroupModalOpen} title="Create new account">
	<NewTransactionGroupForm showTitle={false} onSave={() => (isNewGroupModalOpen = false)} />
</Modal>
