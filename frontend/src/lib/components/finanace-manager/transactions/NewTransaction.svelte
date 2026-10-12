<script lang="ts">
	import { goto } from '$app/navigation';
	import Input from '$lib/components/form/Input.svelte';
	import Select from '$lib/components/form/Select.svelte';
	import { TransactionCreateForm } from '$lib/models/finance-manager/transactions/create-form.svelte';
	import { authStore } from '$lib/stores/auth-store.svelte';
	import { getAccountState } from '$lib/stores/finance-manager/accounts-store.svelte';
	import { getToastState } from '$lib/stores/toast-store.svelte';
	import { useQueryClient } from '@tanstack/svelte-query';

	const accountState = getAccountState();
	const toastState = getToastState();

	const form = new TransactionCreateForm();
	const queryClient = useQueryClient();

	const metadataQuery = accountState.getMeataData();
	const accountsQuery = accountState.getAllAccounts();

	let filteredCategories = $derived.by(() => {
		const meta = metadataQuery.data;
		return meta?.categories?.[form.type] || [];
	});

	const handleSubmit = async (e: SubmitEvent) => {
		const result = await form.submit(e, authStore.token || '');
		if (result) {
			toastState.add('Success', 'Succfully saved the transaction details', 'success');
			queryClient.invalidateQueries({
				queryKey: ['finance-accounts']
			});
			form.resetForm();
		}
	};
</script>

<form onsubmit={handleSubmit} class="grid grid-cols-1 gap-6 lg:grid-cols-3">
	<div class="space-y-6 lg:col-span-2">
		<div class="space-y-5 rounded-xl border border-line bg-panel p-6">
			<div>
				<span class="text-muted text-xs font-semibold">Transaction Type</span>
				<div class="mt-2 grid grid-cols-3 gap-2 rounded-lg bg-page p-1">
					<button
						type="button"
						class="cursor-pointer py-2 text-sm"
						class:font-bold={form.type === 'income'}
						class:income_transaction={form.type === 'income'}
						onclick={() => (form.type = 'income')}
					>
						Income
					</button>
					<button
						type="button"
						class="cursor-pointer py-2 text-sm"
						class:font-bold={form.type === 'expense'}
						class:expense_transaction={form.type === 'expense'}
						onclick={() => (form.type = 'expense')}
					>
						Expense
					</button>
					<button
						type="button"
						class="cursor-pointer py-2 text-sm"
						class:font-bold={form.type === 'transfer'}
						class:transfer_transaction={form.type === 'transfer'}
						onclick={() => (form.type = 'transfer')}
					>
						Transfer
					</button>
				</div>
			</div>

			<div class="grid grid-cols-1 gap-4 sm:grid-cols-2">
				<Input
					id="amount"
					type="number"
					step="0.01"
					bind:value={form.amount}
					label="Amount"
					name="amount"
					classes="sm:col-span-2 space-y-1.5"
					error={form.errors.amount}
					placeholder="250.00"
				/>
				<Input
					id="title"
					bind:value={form.title}
					label="Transaction Title"
					name="title"
					classes="sm:col-span-2 space-y-1.5"
					error={form.errors.title}
					placeholder="Petrol for scooter"
				/>
				{#if form.type === 'transfer'}
					<div>
						<label for="from_account" class="text-sm font-medium">From Account</label>
						<select
							id="from_account"
							bind:value={form.accountId}
							required
							class="mt-1 block w-full rounded border bg-page p-2 text-ink"
						>
							<option value="">-- Source --</option>
							{#each accountsQuery.data || [] as acc}
								<option value={acc.id}>{acc.name} (₹{acc.balance})</option>
							{/each}
						</select>
					</div>
					<div>
						<label for="to_account" class="text-sm font-medium">To Account</label>
						<select
							id="to_account"
							bind:value={form.toAccount}
							required
							class="mt-1 block w-full rounded border bg-page p-2 text-ink"
						>
							<option value="">-- Destination --</option>
							{#each accountsQuery.data || [] as acc}
								{#if String(acc.id) !== String(form.accountId)}
									<option value={acc.id}>{acc.name} (₹{acc.balance})</option>
								{/if}
							{/each}
						</select>
					</div>
				{:else}
					<Select
						id="account"
						name="account"
						label="Account"
						placeholder="-- Choose Account --"
						bind:value={form.accountId}
						classes="sm:col-span-2 space-y-1.5"
						error={form.errors.account_id}
					>
						{#each accountsQuery.data || [] as acc}
							<option value={acc.id}>{acc.name} (₹{acc.balance})</option>
						{/each}
					</Select>
				{/if}

				{#if form.type !== 'transfer'}
					<Select
						id="category"
						name="category"
						label="Category"
						placeholder="-- Choose Category --"
						bind:value={form.category}
						classes="space-y-1.5"
						error={form.errors.category}
					>
						{#each filteredCategories as cat}
							<option value={cat}>{cat}</option>
						{/each}
					</Select>
				{/if}

				<Select
					id="payment_mode"
					name="payment_mode"
					label="Payment Mode"
					placeholder="-- Choose Mode --"
					bind:value={form.paymentMode}
					classes={form.type === 'transfer' ? 'sm:col-span-2 space-y-1.5' : 'space-y-1.5'}
					error={form.errors.payment_mode}
				>
					{#each metadataQuery.data?.payment_modes || [] as mode}
						<option value={mode}>{mode.replaceAll('_', ' ').toUpperCase()}</option>
					{/each}
				</Select>
				{#if form.type === 'expense'}
					<Input
						id="vendor"
						bind:value={form.vendor}
						label="Vendor / Merchant"
						name="vendor"
						classes="sm:col-span-2 space-y-1.5"
						placeholder="HP Petrol pump, 4th Mile"
					/>
				{/if}
			</div>
		</div>
	</div>

	<div class="space-y-6">
		<div class="space-y-4 rounded-xl border border-line bg-panel p-6">
			<Input
				id="datetime"
				type="datetime-local"
				bind:value={form.transactionTime}
				label="Date & Time"
				name="datetime"
				classes="sm:col-span-2 space-y-1.5"
				error={form.errors.transaction_time}
			/>
			<div>
				<label for="description" class="text-sm font-medium">Notes / Description</label>
				<textarea
					id="description"
					rows="3"
					bind:value={form.description}
					class="mt-1 block w-full resize-none rounded border bg-page p-2 text-ink"></textarea>
			</div>

			<button
				type="submit"
				disabled={false}
				class="w-full rounded bg-ink py-2 font-medium text-panel"
			>
				{#if false}Saving...{:else}Save Transaction{/if}
			</button>

			<button
				type="button"
				onclick={() => goto('/app/finance-manager/transactions')}
				class="block w-full rounded border border-line bg-page py-2 text-center text-ink"
			>
				Cancel & Return
			</button>
		</div>
	</div>
</form>
