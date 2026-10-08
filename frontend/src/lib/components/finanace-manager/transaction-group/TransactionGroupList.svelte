<script lang="ts">
	import Moreoptions from '$lib/components/icons/Moreoptions.svelte';
	import Dropdown from '$lib/components/ui/Dropdown.svelte';
	import { getTransactionGroupState } from '$lib/stores/finance-manager/transaction-group-store.svelte';
	import type { TransactionGroup } from '$lib/types/finance';
	import { flip } from 'svelte/animate';
	import { slide } from 'svelte/transition';
	import TransactionGroupDeleteModal from './TransactionGroupDeleteModal.svelte';
	import Modal from '$lib/components/ui/Modal.svelte';
	import TransactionGroupEditForm from './TransactionGroupEditForm.svelte';
	import Alert from '$lib/components/icons/Alert.svelte';

	interface Props {
		filterBy: {
			name: string;
		};
	}

	let { filterBy = $bindable() }: Props = $props();

	const transactionGroupState = getTransactionGroupState();
	let transactionGroupQuery = transactionGroupState.getAllTransactionGroups();
	let isGroupDeleteModalOpen = $state(false);
	let isGroupEditModalOpen = $state(false);
	let selectedTransactionGroup: TransactionGroup | null = $state(null);

	const allTransactionGroup = $derived.by(() => {
		if (transactionGroupQuery.data) {
			let tempGroups = transactionGroupQuery.data;
			if (filterBy.name) {
				tempGroups = tempGroups.filter((group) =>
					group.name.toLowerCase().includes(filterBy.name.toLowerCase())
				);
			}
			return tempGroups;
		}
	});

	function handleOnDelete(e: MouseEvent, group: TransactionGroup) {
		e.stopPropagation();
		isGroupDeleteModalOpen = !isGroupDeleteModalOpen;
		selectedTransactionGroup = group;
	}

	function handleOnEdit(e: MouseEvent, group: TransactionGroup) {
		e.stopPropagation();
		isGroupEditModalOpen = !isGroupEditModalOpen;
		selectedTransactionGroup = group;
	}
</script>

{#snippet groupOptions(group: TransactionGroup)}
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
						onclick={(e) => handleOnEdit(e, group)}
						class="block w-full cursor-pointer rounded-md px-4 py-2 text-left text-sm hover:bg-page"
					>
						Edit
					</button>
				</div>
				<button
					onclick={(e) => handleOnDelete(e, group)}
					class="block w-full cursor-pointer rounded-md px-4 py-2 text-left text-sm text-red-600 hover:bg-red-50"
				>
					Delete
				</button>
			</div>
		{/snippet}
	</Dropdown>
{/snippet}

<div class="grid grid-cols-1 gap-4 @lg:grid-cols-2 @3xl:grid-cols-3">
	{#if transactionGroupQuery.isLoading}
		<div>Loading..</div>
	{:else}
		{#each allTransactionGroup as group (group.id)}
			<article
				transition:slide={{ duration: 300 }}
				animate:flip={{ duration: 300 }}
				class="rounded-lg border border-line bg-panel p-5"
			>
				<div class="flex items-start justify-between gap-3">
					<h2 class="font-semibold">{group.name}</h2>
					{@render groupOptions(group)}
				</div>
				<p class="text-muted mt-1 text-sm">{group.description}</p>
			</article>
		{:else}
			<div class="flex items-center gap-1.5 text-hot">
				<Alert />
				<p>No records found</p>
			</div>
		{/each}
	{/if}
</div>

<TransactionGroupDeleteModal
	bind:isOpen={isGroupDeleteModalOpen}
	transactionGroup={selectedTransactionGroup!}
/>
<Modal title="Edit Tranaction Group" bind:isOpen={isGroupEditModalOpen}>
	<TransactionGroupEditForm
		transactionGroup={selectedTransactionGroup!}
		onSave={() => (isGroupEditModalOpen = false)}
	/>
</Modal>
