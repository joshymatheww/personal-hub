<script lang="ts">
	import { goto } from '$app/navigation';
	import { LoginForm } from '$lib/models/login-form.svelte';
	import Input from '../form/Input.svelte';
	import SubmitButton from '../form/SubmitButton.svelte';
	import EyeClosed from '../icons/EyeClosed.svelte';
	import EyeOpen from '../icons/EyeOpen.svelte';

	const form = new LoginForm();
	let togglePassword = $state(false);

	const handleSubmit = async (e: SubmitEvent) => {
		const result = await form.submit(e);
		if (result) {
			goto('/app');
		}
	};
</script>

<form class="mt-8 space-y-5" onsubmit={handleSubmit}>
	{#if form.errors.general}
		<div class="rounded-md bg-hot/10 p-3 text-sm font-medium text-hot">
			{form.errors.general}
		</div>
	{/if}

	<Input
		id="email"
		name="email"
		type="email"
		label="Email"
		bind:value={form.email}
		placeholder="you@example.com"
		required
		error={form.errors.email}
	/>

	<div class="space-y-1.5">
		<div class="relative">
			<Input
				id="password"
				name="password"
				type={!togglePassword ? 'password' : 'text'}
				label="Password"
				bind:value={form.passowrd}
				autocomplete="current-password"
				required
				placeholder="••••••••"
				error={form.errors.password}
			/>
			<button
				type="button"
				aria-label="Show password"
				aria-pressed="false"
				class="text-muted absolute top-11.25 right-2.5 grid h-7 w-7 -translate-y-1/2 place-items-center rounded-md hover:bg-page"
				onclick={() => (togglePassword = !togglePassword)}
			>
				{#if !togglePassword}
					<EyeOpen />
				{:else}
					<EyeClosed />
				{/if}
			</button>
		</div>
	</div>

	<SubmitButton
		title={form.isSubmitting ? 'Logging in ...' : 'Log in'}
		disabled={form.isSubmitting || !form.isValid}
	/>
</form>
