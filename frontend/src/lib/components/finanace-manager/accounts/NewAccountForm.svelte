<script lang="ts">
	import Input from '$lib/components/form/Input.svelte';
	import SubmitButton from '$lib/components/form/SubmitButton.svelte';
	import Save from '$lib/components/icons/Save.svelte';
	import { AccountForm } from '$lib/models/account-form.svelte';
	import { authStore } from '$lib/stores/auth-store.svelte';
	import { getFinanceState } from '$lib/stores/finance-store.svelte';
	import { useQueryClient } from '@tanstack/svelte-query';

	const form = new AccountForm();
	const financeState = getFinanceState();
	const queryClient = useQueryClient();

	const handleSubmit = async (e: SubmitEvent) => {
		const result = await form.submit(e, authStore.token || '');
		if (result) {
			queryClient.invalidateQueries({
				queryKey: ['finance-accounts']
			});
			form.resetForm();
		}
	};
</script>

<aside class="h-fit rounded-lg border border-line bg-panel p-5 sm:p-6">
	<form onsubmit={handleSubmit}>
		<h2 class="mb-3 font-semibold">Add an account</h2>
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

		<div class="my-4">
			<span class="text-muted text-sm">Type</span>
			<div class="mt-2 flex flex-wrap gap-2">
				{#each financeState.accountTypes as category}
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
			title={form.isSubmitting ? 'Saving...' : 'Save Account'}
			disabled={form.isSubmitting}
		>
			<Save />
		</SubmitButton>
	</form>
</aside>
