<script lang="ts">
	import Input from '$lib/components/form/Input.svelte';
	import SubmitButton from '$lib/components/form/SubmitButton.svelte';
	import Save from '$lib/components/icons/Save.svelte';
	import { TransactionGroupForm } from '$lib/models/finance-manager/transaction-group/create-form.svelte';
	import { authStore } from '$lib/stores/auth-store.svelte';
	import { getToastState } from '$lib/stores/toast-store.svelte';
	import { useQueryClient } from '@tanstack/svelte-query';

	interface Props {
		showTitle?: boolean;
		onSave?: () => void;
	}

	let { showTitle = true, onSave }: Props = $props();

	const form = new TransactionGroupForm();
	const queryClient = useQueryClient();
	const toastState = getToastState();

	const handleSubmit = async (e: SubmitEvent) => {
		const result = await form.submit(e, authStore.token || '');
		if (result) {
			if (!showTitle) {
				onSave?.();
			}
			queryClient.invalidateQueries({
				queryKey: ['finance-transaction-group']
			});
			form.resetForm();
			toastState.add('Success', 'Successfully saved the transaction group details', 'success');
		}
	};
</script>

<aside class="h-fit rounded-lg border border-line bg-panel p-5 sm:p-6">
	<form onsubmit={handleSubmit}>
		{#if showTitle}
			<h2 class="mb-3 font-semibold">Add an account</h2>
		{/if}
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
				placeholder="eg: Hospital Expenses"
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
			/>
		</div>

		<SubmitButton
			title={form.isSubmitting ? 'Saving...' : 'Save Group'}
			disabled={form.isSubmitting}
		>
			<Save />
		</SubmitButton>
	</form>
</aside>
