<script lang="ts">
	import './layout.css';
	import favicon from '$lib/assets/favicon.svg';
	import { QueryCache, QueryClient, QueryClientProvider } from '@tanstack/svelte-query';
	import { SvelteQueryDevtools } from '@tanstack/svelte-query-devtools';
	import { authStore } from '$lib/stores/auth-store.svelte';
	import { goto } from '$app/navigation';

	let { children } = $props();

	const queryClient = new QueryClient({
		defaultOptions: {
			queries: {
				staleTime: 1000 * 60 * 5,
				refetchOnWindowFocus: false
			}
		},
		queryCache: new QueryCache({
			onError: (error: any, query) => {
				if (error.status === 401 && error.errors === 'Invalid or expired token') {
					authStore.logout();
					goto('/');
				}
			}
		})
	});
</script>

<svelte:head><link rel="icon" href={favicon} /></svelte:head>

<QueryClientProvider client={queryClient}>
	{@render children()}
	<SvelteQueryDevtools />
</QueryClientProvider>
