<script lang="ts">
	import { authStore } from '$lib/stores/auth-store.svelte';
	import DownArrow from '../icons/DownArrow.svelte';

	const getAvataIcon = (firstName: string, lastName: string | null = '') => {
		const firstInitial = firstName.charAt(0) || '';
		const lastInitial = lastName?.charAt(0) || '';
		return (firstInitial + lastInitial).toUpperCase();
	};
</script>

{#if authStore.token && authStore.isLoadingUser}
	<div class="flex animate-pulse space-x-4">
		<div class="size-8 rounded-full bg-gray-200"></div>
		<div class="flex-1 space-y-6 py-1">
			<div class="h-2 rounded bg-gray-200"></div>
		</div>
	</div>
{:else}
	<button
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
	</button>
{/if}
