<script lang="ts">
	import { page } from '$app/state';
	import Bank from '$lib/components/icons/Bank.svelte';
	import TransactionsGroup from '$lib/components/icons/TransactionsGroup.svelte';

	let { children } = $props();
</script>

<div class="grid w-full grid-cols-1 gap-8 lg:grid-cols-[220px_1fr]">
	<!-- Left Nested Sub-Sidebar Section -->
	<aside
		class="flex flex-col justify-start gap-3 text-sm sm:flex-row sm:justify-center lg:flex-col lg:justify-start"
	>
		<a
			href="/app/finance-manager/settings/accounts"
			class="flex items-center gap-1.5"
			class:font-bold={page.url.pathname === '/app/finance-manager/settings/accounts'}
		>
			<Bank />
			<span>Accounts</span>
		</a>
		<a
			href="/app/finance-manager/settings/transactions-groups"
			class="flex items-center gap-1.5"
			class:font-bold={page.url.pathname === '/app/finance-manager/settings/transactions-groups'}
		>
			<TransactionsGroup />
			<span>Transactions Groups</span>
		</a>
	</aside>

	<!-- Right Main Card Content Section -->
	<main class="min-h-100 rounded-xl border border-line bg-panel p-6">
		{@render children()}
	</main>
</div>
