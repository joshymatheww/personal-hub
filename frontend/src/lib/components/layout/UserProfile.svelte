<script lang="ts">
	import { goto } from '$app/navigation';
	import { authStore } from '$lib/stores/auth-store.svelte';
	import DownArrow from '../icons/DownArrow.svelte';
	import Dropdown from '../ui/Dropdown.svelte';

	const getAvataIcon = (firstName: string, lastName: string | null = '') => {
		const firstInitial = firstName.charAt(0) || '';
		const lastInitial = lastName?.charAt(0) || '';
		return (firstInitial + lastInitial).toUpperCase();
	};

	function handleClick() {
		authStore.logout();
		goto('/');
	}
</script>

{#if authStore.token && authStore.isLoadingUser}
	<div class="flex animate-pulse space-x-4">
		<div class="size-8 rounded-full bg-gray-200"></div>
		<div class="flex-1 space-y-6 py-1">
			<div class="h-2 rounded bg-gray-200"></div>
		</div>
	</div>
{:else}
	<Dropdown>
		{#snippet trigger()}
			<div
				class="ml-1 flex items-center gap-1 rounded-md py-1 pr-2 pl-1 hover:bg-page"
				aria-label="Account"
			>
				<span
					class="text-muted grid h-8 w-8 place-items-center rounded-full bg-page text-xs font-semibold"
				>
					{authStore.user
						? getAvataIcon(authStore.user.first_name, authStore.user.last_name ?? '')
						: 'AU'}
				</span>
				<DownArrow />
			</div>
		{/snippet}
		{#snippet children()}
			<div class="py-1">
				<a
					href="/app/settings"
					class="block rounded-lg px-4 py-2 text-sm text-zinc-700 hover:bg-zinc-100 dark:text-zinc-200 dark:hover:bg-zinc-800"
				>
					Settings
				</a>
				<button
					onclick={handleClick}
					class="block w-full cursor-pointer rounded-lg px-4 py-2 text-left text-sm text-red-600 hover:bg-red-50 dark:hover:bg-red-950/50"
				>
					Sign out
				</button>
			</div>
		{/snippet}
	</Dropdown>
{/if}
