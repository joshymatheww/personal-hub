<script lang="ts">
	import Input from '$lib/components/form/Input.svelte';
	import SubmitButton from '$lib/components/form/SubmitButton.svelte';
	import Save from '$lib/components/icons/Save.svelte';
	import { TransactionGroupUpdateForm } from '$lib/models/finance-manager/transaction-group/edit-form.svelte';
	import { authStore } from '$lib/stores/auth-store.svelte';
	import { getToastState } from '$lib/stores/toast-store.svelte';
	import type { TransactionGroup } from '$lib/types/finance';
	import { useQueryClient } from '@tanstack/svelte-query';

	interface Props {
		onSave: () => void;
		transactionGroup: TransactionGroup;
	}

	let { onSave, transactionGroup }: Props = $props();

	const form = $derived(new TransactionGroupUpdateForm(transactionGroup));
	const queryClient = useQueryClient();
	const toastState = getToastState();

	const handleSubmit = async (e: SubmitEvent) => {
		const result = await form.submit(e, authStore.token || '');
		if (result) {
			queryClient.invalidateQueries({
				queryKey: ['finance-transaction-group']
			});
			toastState.add('Success', 'Successfully updated the transaction group details', 'success');
			onSave();
		}
	};
</script>

<aside class="h-fit rounded-lg border border-line bg-panel p-5 sm:p-6">
	<form onsubmit={handleSubmit}>
		{#if form.errors.general}
			<div class="rounded-md bg-hot/10 p-3 text-sm font-medium text-hot">
				{form.errors.general}
			</div>
		{/if}
		<div>
			<Input
				id="name"
				name="name"
				label="Name"
				placeholder="eg: SBI Thalassery"
				bind:value={form.name}
				error={form.errors.name}
			/>
		</div>

		<div class="my-3">
			<Input
				id="description"
				name="description"
				label="description"
				bind:value={form.description}
				error={form.errors.description}
			/>
		</div>

		<SubmitButton
			title={form.isSubmitting ? 'Updating...' : 'Update Group'}
			disabled={form.isSubmitting}
		>
			<Save />
		</SubmitButton>
	</form>
</aside>
