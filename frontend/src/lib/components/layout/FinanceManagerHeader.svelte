<script lang="ts">
	import { page } from '$app/state';
	import Dashboard from '../icons/Dashboard.svelte';
	import List from '../icons/List.svelte';
	import Plus from '../icons/Plus.svelte';
	import Settings from '../icons/Settings.svelte';
</script>

<div class="mb-6 border-b border-line backdrop-blur">
	<div class="flex h-16 items-center gap-2">
		<ul class="hidden items-center gap-6 text-sm md:flex">
			<li>
				<a
					href="/app/finance-manager"
					class="flex items-center gap-1.5"
					class:font-bold={page.url.pathname === '/app/finance-manager'}
				>
					<Dashboard />
					<span>Dashboard</span>
				</a>
			</li>
			<li>
				<a
					href="/app/finance-manager/transactions"
					class="flex items-center gap-1.5"
					class:font-bold={page.url.pathname === '/app/finance-manager/transactions'}
				>
					<List />
					<span>Transactions</span>
				</a>
			</li>
			<li>
				<a
					href="/app/finance-manager/settings/accounts"
					class="flex items-center gap-1.5"
					class:font-bold={page.url.pathname === '/app/finance-manager/settings/accounts'}
				>
					<Settings />
					<span>Settings</span>
				</a>
			</li>
		</ul>
		<div class="ml-auto flex items-center gap-1">
			<a
				href="/app/finance-manager/transactions/new"
				class="mr-1 hidden items-center gap-1.5 rounded-md bg-ink px-4 py-2 text-sm font-medium text-panel hover:bg-ink/90 sm:flex"
			>
				<Plus />
				<span>New Transaction</span>
			</a>
		</div>
	</div>
</div>
