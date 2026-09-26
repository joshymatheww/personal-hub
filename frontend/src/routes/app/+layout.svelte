<script lang="ts">
	import { page } from '$app/state';
	import Sidebar from '$lib/components/layout/Sidebar.svelte';

	let { children } = $props();
</script>

<!-- Permanent Navigation Sidebar -->
<Sidebar />

<div class="lg:pl-16">
	<!-- Dynamic Dashboard Content View -->
	<main class="px-4 py-8 pb-24 sm:px-6 lg:px-8 lg:pb-8">
		{@render children()}
	</main>
</div>
