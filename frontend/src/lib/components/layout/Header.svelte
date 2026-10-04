<script lang="ts">
	import AlarmOne from '../icons/AlarmOne.svelte';
	import Home from '../icons/Home.svelte';
	import List from '../icons/List.svelte';
	import UserProfile from './UserProfile.svelte';
</script>

<header class="sticky top-0 z-20 border-b border-line bg-panel/90 backdrop-blur">
	<div class="flex h-16 items-center gap-2 px-4 sm:px-6 lg:px-8">
		<button
			type="button"
			class="text-muted -ml-1 grid h-10 w-10 place-items-center rounded-md hover:bg-page lg:hidden"
			aria-label="Open menu"
			aria-expanded="false"
			data-menu-toggle
		>
			<svg viewBox="0 0 24 24" class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="1.8"
				><path d="M4 7h16M4 12h16M4 17h16" /></svg
			>
		</button>

		<nav class="hidden items-center gap-6 text-sm md:flex">
			<a href="/app" class="top-link text-muted flex items-center gap-1.5 hover:text-ink">
				<Home />
				<span>Home</span>
			</a>
			<a
				href="/app/finance-manager/transactions"
				class="top-link text-muted flex items-center gap-1.5 hover:text-ink"
			>
				<List />
				<span>Transactions</span>
			</a>
			<a
				href="/app/workouts-manager/sessions"
				class="top-link text-muted flex items-center gap-1.5 hover:text-ink"
			>
				<AlarmOne />
				<span>Sessions</span>
			</a>
		</nav>

		<div class="ml-auto flex items-center gap-1">
			<button
				class="text-muted grid h-10 w-10 place-items-center rounded-md hover:bg-page"
				aria-label="Search"
			>
				<svg
					viewBox="0 0 24 24"
					class="h-5 w-5"
					fill="none"
					stroke="currentColor"
					stroke-width="1.7"><circle cx="11" cy="11" r="6" /><path d="M20 20l-3.5-3.5" /></svg
				>
			</button>
			<UserProfile />
		</div>
	</div>

	<nav class="hidden border-t border-line px-4 pt-2 pb-4 text-sm lg:!hidden" data-menu-panel>
		<a href="#/dashboard" class="block rounded-md px-3 py-2 hover:bg-page">Dashboard</a>
		<a href="#/sessions" class="block rounded-md px-3 py-2 hover:bg-page">Sessions</a>
		<a href="#/session-detail" class="block rounded-md px-3 py-2 hover:bg-page">New session</a>
		<a href="#/exercises" class="block rounded-md px-3 py-2 hover:bg-page">Exercises</a>
		<a href="#/recovery" class="block rounded-md px-3 py-2 hover:bg-page">Recovery</a>
	</nav>
</header>
