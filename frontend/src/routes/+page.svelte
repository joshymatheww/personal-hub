<script lang="ts">
	import Dumbell from '$lib/components/icons/Dumbell.svelte';
	import LoginForm from '$lib/components/layout/LoginForm.svelte';
	import WelcomeMessage from '$lib/components/layout/WelcomeMessage.svelte';
</script>

<svelte:head>
	<title>Welcome to Workout log</title>
</svelte:head>

<div class="grid min-h-dvh lg:grid-cols-2">
	<WelcomeMessage />
	<div class="flex items-center justify-center px-4 py-12 sm:px-6">
		<div class="w-full max-w-sm">
			<div class="mb-8 flex items-center gap-2 lg:hidden">
				<span class="grid h-9 w-9 place-items-center rounded-md bg-rail text-white">
					<Dumbell />
				</span>
				<span class="font-display text-lg font-semibold">Workout log</span>
			</div>
			<h1 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">Welcome back</h1>
			<p class="text-muted mt-1.5">Log in to pick up where you left off.</p>
			<LoginForm />
		</div>
	</div>
</div>
