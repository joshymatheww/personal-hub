<script lang="ts">
	import Moreoptions from '$lib/components/icons/Moreoptions.svelte';
	import Dropdown from '$lib/components/ui/Dropdown.svelte';
	import { getAccountState } from '$lib/stores/finance-manager/accounts-store.svelte';
	import type { Account } from '$lib/types/finance';
	import { flip } from 'svelte/animate';
	import { slide } from 'svelte/transition';
	import AccountDeleteModal from './AccountDeleteModal.svelte';
	import Modal from '$lib/components/ui/Modal.svelte';
	import AccountEditForm from './AccountEditForm.svelte';
	import Alert from '$lib/components/icons/Alert.svelte';

	interface Props {
		filterBy: {
			name: string;
			type: string;
		};
	}

	let { filterBy = $bindable() }: Props = $props();

	const accountState = getAccountState();
	let accountsQuery = accountState.getAllAccounts();
	let isAccountDeleteModalOpen = $state(false);
	let isAccountEditModalOpen = $state(false);
	let selectedAccount: Account | null = $state(null);

	const allAccounts = $derived.by(() => {
		if (accountsQuery.data) {
			let tempAccounts = accountsQuery.data;
			if (filterBy.name) {
				tempAccounts = tempAccounts.filter((account) =>
					account.name.toLowerCase().includes(filterBy.name.toLowerCase())
				);
			}
			if (filterBy.type) {
				tempAccounts = tempAccounts.filter((account) => account.type === filterBy.type);
			}
			return tempAccounts;
		}
	});

	function handleOnDelete(e: MouseEvent, account: Account) {
		e.stopPropagation();
		isAccountDeleteModalOpen = !isAccountDeleteModalOpen;
		selectedAccount = account;
	}

	function handleOnEdit(e: MouseEvent, account: Account) {
		e.stopPropagation();
		isAccountEditModalOpen = !isAccountEditModalOpen;
		selectedAccount = account;
	}
</script>

{#snippet accountOptions(account: Account)}
	<Dropdown>
		{#snippet trigger()}
			<div
				class="text-muted -mt-1 -mr-2 grid h-8 w-8 shrink-0 place-items-center rounded-md hover:bg-page"
				aria-label="Options"
			>
				<Moreoptions />
			</div>
		{/snippet}
		{#snippet children()}
			<div class="py-1">
				<div class="mb-1 border-b border-line pb-1">
					<button
						onclick={(e) => handleOnEdit(e, account)}
						class="block w-full cursor-pointer rounded-md px-4 py-2 text-left text-sm hover:bg-page"
					>
						Edit
					</button>
					{#if account.type === 'bank_account'}
						<button
							class="block w-full cursor-pointer rounded-md px-4 py-2 text-left text-sm hover:bg-page"
						>
							Transfer
						</button>
					{/if}
				</div>
				<button
					onclick={(e) => handleOnDelete(e, account)}
					class="block w-full cursor-pointer rounded-md px-4 py-2 text-left text-sm text-red-600 hover:bg-red-50"
				>
					Delete
				</button>
			</div>
		{/snippet}
	</Dropdown>
{/snippet}

<div class="grid grid-cols-1 gap-4 @lg:grid-cols-2 @3xl:grid-cols-3">
	{#if accountsQuery.isLoading}
		<div>Loading..</div>
	{:else}
		{#each allAccounts as account (account.id)}
			<article
				transition:slide={{ duration: 300 }}
				animate:flip={{ duration: 300 }}
				class="rounded-lg border border-line bg-panel p-5"
			>
				<div class="flex items-start justify-between gap-3">
					<h2 class="font-semibold">{account.name}</h2>
					{@render accountOptions(account)}
				</div>
				<p class="text-muted mt-1 text-sm">{account.balance}</p>
				<div class="mt-3 flex flex-wrap gap-1.5 text-xs">
					<span class="rounded-full bg-ink px-2.5 py-1 font-medium text-panel capitalize">
						{account.type.replaceAll('_', ' ')}
					</span>
				</div>
			</article>
		{:else}
			<div class="flex items-center gap-1.5 text-hot">
				<Alert />
				<p>No records found</p>
			</div>
		{/each}
	{/if}
</div>

<AccountDeleteModal bind:isOpen={isAccountDeleteModalOpen} account={selectedAccount!} />
<Modal title="Edit Account" bind:isOpen={isAccountEditModalOpen}>
	<AccountEditForm account={selectedAccount!} onSave={() => (isAccountEditModalOpen = false)} />
</Modal>
