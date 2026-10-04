<script lang="ts">
	import { page } from '$app/state';
</script>

<div class="mb-6 border-b border-line backdrop-blur">
	<div class="flex h-16 items-center gap-2">
		<ul class="hidden items-center gap-6 text-sm md:flex">
			<li>
				<a
					href="/app/finance-manager"
					class:font-bold={page.url.pathname === '/app/finance-manager'}
				>
					Dashboard
				</a>
			</li>
			<li>
				<a
					href="/app/finance-manager/transactions"
					class:font-bold={page.url.pathname === '/app/finance-manager/transactions'}
				>
					Transactions
				</a>
			</li>
			<li>
				<a
					href="/app/finance-manager/settings/accounts"
					class:font-bold={page.url.pathname === '/app/finance-manager/settings/accounts'}
				>
					Settings
				</a>
			</li>
		</ul>
		<div class="ml-auto flex items-center gap-1">
			<a
				href="#/session-detail"
				class="mr-1 hidden rounded-md bg-ink px-4 py-2 text-sm font-medium text-panel hover:bg-ink/90 sm:block"
				>New Transaction</a
			>
		</div>
	</div>
</div>
