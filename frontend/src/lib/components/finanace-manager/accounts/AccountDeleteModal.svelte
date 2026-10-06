<script lang="ts">
	import { goto } from '$app/navigation';
	import { deleteResource } from '$lib/apis/http';
	import Modal from '$lib/components/ui/Modal.svelte';
	import { authStore } from '$lib/stores/auth-store.svelte';
	import { getToastState } from '$lib/stores/toast-store.svelte';
	import type { Account } from '$lib/types/finance';
	import { useQueryClient } from '@tanstack/svelte-query';

	interface Props {
		isOpen: boolean;
		account: Account;
	}

	let { isOpen = $bindable(false), account }: Props = $props();
	const toastState = getToastState();
	const queryClient = useQueryClient();

	async function handleDelete() {
		if (authStore.token) {
			try {
				const result = await deleteResource(authStore.token, `finance/accounts/${account.id}`);
				if (result) {
					queryClient.invalidateQueries({
						queryKey: ['finance-accounts']
					});
					toastState.add('Success', 'Succesfuuly removed the account', 'success');
				} else {
					toastState.add('Error', 'Somthing went wrong', 'error');
				}
			} catch (error: any) {
				toastState.add('Error', error.errors, 'error');
				if (error.status === 401) {
					authStore.logout();
					goto('/');
				}
			} finally {
				isOpen = false;
			}
		}
	}
</script>

<Modal bind:isOpen title="Confirm Deletion">
	<p class="text-muted">
		This action is permanent and cannot be undone. All data records linked to this account token
		will be removed completely from the production database arrays instantly.
	</p>
	{#snippet footer()}
		<button
			type="button"
			onclick={() => (isOpen = false)}
			class="cursor-pointer rounded-md border border-line bg-panel px-4 py-2 text-sm font-medium text-ink hover:bg-page"
		>
			Cancel
		</button>
		<button
			type="button"
			onclick={handleDelete}
			class="cursor-pointer rounded-md bg-hot px-4 py-2 text-sm font-semibold text-white hover:opacity-90"
		>
			Yes, delete data
		</button>
	{/snippet}
</Modal>
