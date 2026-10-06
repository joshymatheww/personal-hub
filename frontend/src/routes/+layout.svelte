<script lang="ts">
	import './layout.css';
	import favicon from '$lib/assets/favicon.ico';
	import { QueryCache, QueryClient, QueryClientProvider } from '@tanstack/svelte-query';
	import { SvelteQueryDevtools } from '@tanstack/svelte-query-devtools';
	import { authStore } from '$lib/stores/auth-store.svelte';
	import { goto } from '$app/navigation';
	import Toaster from '$lib/components/ui/Toaster.svelte';
	import { setToastState } from '$lib/stores/toast-store.svelte';

	let { children } = $props();

	setToastState();

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

<Toaster />

<QueryClientProvider client={queryClient}>
	{@render children()}
	<SvelteQueryDevtools />
</QueryClientProvider>
