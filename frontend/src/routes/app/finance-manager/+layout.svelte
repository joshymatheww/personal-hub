<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/state';
	import Menu from '$lib/components/icons/Menu.svelte';
	import FinanceManagerHeader from '$lib/components/layout/FinanceManagerHeader.svelte';
	import { authStore } from '$lib/stores/auth-store.svelte';
	import { setAccountState } from '$lib/stores/finance-manager/accounts-store.svelte';
	import { setTransactionGroupState } from '$lib/stores/finance-manager/transaction-group-store.svelte';
	import { format } from 'date-fns';
	import { onMount } from 'svelte';

	let { children } = $props();
	let toggleMenu = $state(false);
	let sectionRef: HTMLElement | undefined = $state();

	setAccountState();
	setTransactionGroupState();

	function handleWindowResize() {
		if (sectionRef) {
			if (sectionRef.clientWidth >= 640) {
				toggleMenu = false;
			}
		}
	}

	onMount(async () => {
		if (!authStore.token) {
			authStore.logout();
			goto('/');
		}
	});
</script>

<svelte:window onresize={handleWindowResize} />

<section id="dashboard" bind:this={sectionRef}>
	<div class="mb-1 flex flex-wrap items-baseline justify-between gap-x-6 gap-y-2">
		<div class="flex items-center gap-2">
			<button
				class="text-muted -ml-1 grid h-10 w-10 place-items-center rounded-md hover:bg-white sm:hidden"
				onclick={() => (toggleMenu = !toggleMenu)}
			>
				<Menu />
			</button>
			<h1 class="font-display text-3xl font-bold tracking-tight sm:text-4xl">Finance Manager</h1>
		</div>
		<span class="text-sm font-semibold tabular-nums">
			{format(new Date(), 'EEEE, d LLLL')}
		</span>
		<nav
			class="w-full items-center justify-between border-t border-line px-4 pt-2 pb-1 text-sm"
			class:flex={toggleMenu}
			class:hidden={!toggleMenu}
		>
			<a
				href="/app/finance-manager"
				class="block rounded-md px-3 py-2 hover:bg-page"
				class:is_active_sub={page.url.pathname === '/app/finance-manager'}
			>
				Dashboard
			</a>
			<a
				href="/app/finance-manager/transactions"
				class="block rounded-md px-3 py-2 hover:bg-page"
				class:is_active_sub={page.url.pathname === '/app/finance-manager/transactions'}
			>
				Transactions
			</a>
			<a
				href="/app/finance-manager/settings/accounts"
				class="block rounded-md px-3 py-2 hover:bg-page"
				class:is_active_sub={page.url.pathname === '/app/finance-manager/settings/accounts'}
			>
				Settings
			</a>
		</nav>
	</div>
	<FinanceManagerHeader />
	{@render children()}
</section>
