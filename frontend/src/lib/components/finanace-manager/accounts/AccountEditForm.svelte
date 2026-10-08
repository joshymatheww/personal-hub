<script lang="ts">
	import Input from '$lib/components/form/Input.svelte';
	import SubmitButton from '$lib/components/form/SubmitButton.svelte';
	import Save from '$lib/components/icons/Save.svelte';
	import { AccountUpdateForm } from '$lib/models/finance-manager/accounts/edit-form.svelte';
	import { authStore } from '$lib/stores/auth-store.svelte';
	import { getAccountState } from '$lib/stores/finance-manager/accounts-store.svelte';
	import { getToastState } from '$lib/stores/toast-store.svelte';
	import type { Account } from '$lib/types/finance';
	import { useQueryClient } from '@tanstack/svelte-query';

	interface Props {
		onSave: () => void;
		account: Account;
	}

	let { onSave, account }: Props = $props();

	const form = $derived(new AccountUpdateForm(account));
	const accountState = getAccountState();
	const queryClient = useQueryClient();
	const toastState = getToastState();

	const handleSubmit = async (e: SubmitEvent) => {
		const result = await form.submit(e, authStore.token || '');
		if (result) {
			queryClient.invalidateQueries({
				queryKey: ['finance-accounts']
			});
			toastState.add('Success', 'Succfully updated the account details', 'success');
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
				id="balance"
				name="balance"
				label="Balance"
				bind:value={form.balance}
				error={form.errors.balance}
			/>
		</div>

		<div class="mt-4 mb-6">
			<span class="text-muted text-sm">Type</span>
			<div class="mt-2 flex flex-wrap gap-2">
				{#each accountState.accountTypes as category}
					<button
						type="button"
						class="hover:border-muted cursor-pointer rounded-full border border-line px-3 py-1.5 text-xs capitalize"
						onclick={() => (form.type = category)}
						class:bg-ink={form.type === category}
						class:bg-page={form.type !== category}
						class:text-panel={form.type === category}
					>
						{category.replaceAll('_', ' ')}
					</button>
				{/each}
			</div>
			{#if form.errors.type}
				<p class="mt-2 text-xs text-hot">{form.errors.type}</p>
			{/if}
		</div>

		<SubmitButton
			title={form.isSubmitting ? 'Updating...' : 'Update Account'}
			disabled={form.isSubmitting}
		>
			<Save />
		</SubmitButton>
	</form>
</aside>
