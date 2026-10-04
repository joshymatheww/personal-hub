<script lang="ts">
	import { goto } from '$app/navigation';
	import FinanceManagerHeader from '$lib/components/layout/FinanceManagerHeader.svelte';
	import { authStore } from '$lib/stores/auth-store.svelte';
	import { getFinanceState, setFinanceState } from '$lib/stores/finance-store.svelte';
	import { format } from 'date-fns';
	import { onMount } from 'svelte';

	let { children } = $props();

	setFinanceState();

	onMount(async () => {
		if (!authStore.token) {
			authStore.logout();
			goto('/');
		}
	});
</script>

<section id="dashboard">
	<div class="mb-1 flex flex-wrap items-baseline justify-between gap-x-6 gap-y-2">
		<h1 class="font-display text-3xl font-bold tracking-tight sm:text-4xl">Finance Manager</h1>
		<span class="text-sm font-semibold tabular-nums">
			{format(new Date(), 'EEEE, d LLLL')}
		</span>
	</div>
	<FinanceManagerHeader />
	{@render children()}
</section>
