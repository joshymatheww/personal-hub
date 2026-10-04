<script lang="ts">
	import { page } from '$app/state';

	let { children } = $props();
</script>

<div class="grid w-full grid-cols-1 gap-8 lg:grid-cols-[220px_1fr]">
	<!-- Left Nested Sub-Sidebar Section -->
	<aside
		class="flex flex-col justify-start gap-1 text-sm sm:flex-row sm:justify-center lg:flex-col lg:justify-start"
	>
		<a
			href="/app/finance-manager/settings/accounts"
			class:font-bold={page.url.pathname === '/app/finance-manager/settings/accounts'}
		>
			Accounts
		</a>
		<a
			href="/app/finance-manager/settings/transactions-groups"
			class:font-bold={page.url.pathname === '/app/finance-manager/settings/transactions-groups'}
		>
			Transactions Groups
		</a>
	</aside>

	<!-- Right Main Card Content Section -->
	<main class="min-h-100 rounded-xl border border-line bg-panel p-6">
		{@render children()}
	</main>
</div>
