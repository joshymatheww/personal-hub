<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/state';
	import { getCurrentuser } from '$lib/apis/auth';
	import Header from '$lib/components/layout/Header.svelte';
	import Sidebar from '$lib/components/layout/Sidebar.svelte';
	import { authStore } from '$lib/stores/auth-store.svelte';
	import { onDestroy, onMount } from 'svelte';

	let { children } = $props();
	let logoutTimer: ReturnType<typeof setTimeout>;

	function startAutoLogoutTimer() {
		if (logoutTimer) clearTimeout(logoutTimer);
		const thirtyMinutes = 30 * 60 * 1000;

		logoutTimer = setTimeout(() => {
			alert('Your session has expired. Please login..');
			authStore.logout();
			goto('/');
		}, thirtyMinutes);
	}

	$effect(() => {
		const currentRoute = page.url.pathname;
		const isPublicRoute = currentRoute === '/';

		if (!isPublicRoute && !authStore.token) {
			goto('/');
		}
	});

	onMount(async () => {
		if (!authStore.token) {
			authStore.logout();
			goto('/');
		} else {
			try {
				authStore.isLoadingUser = true;
				const profile = await getCurrentuser(authStore.token);
				authStore.setUser(profile);
				startAutoLogoutTimer();
			} catch (error) {
				authStore.logout();
				goto('/');
			}
		}
	});

	onDestroy(() => {
		if (logoutTimer) clearTimeout(logoutTimer);
	});
</script>

<Sidebar />

<div class="lg:pl-16">
	<Header />
	<main class="px-4 py-8 pb-24 sm:px-6 lg:px-8 lg:pb-8">
		{@render children()}
	</main>
</div>
