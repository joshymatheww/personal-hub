<script lang="ts">
	import type { HTMLInputAttributes } from 'svelte/elements';

	type Props = {
		id: string;
		name: string;
		label: string;
		value: string | number;
		error?: string;
		classes?: string;
	} & HTMLInputAttributes;

	let {
		id,
		name,
		label,
		value = $bindable(),
		error = '',
		classes = 'space-y-1.5',
		...restProps
	}: Props = $props();
</script>

<div class={classes}>
	<label for={id} class="block font-medium">{label}</label>
	<input
		{id}
		{name}
		bind:value
		class="placeholder:text-muted/60 w-full rounded-md border bg-page px-3.5 py-2.5 transition-colors
           {error ? 'border-hot focus:ring-hot' : 'border-line focus:ring-0'}"
		{...restProps}
	/>
	{#if error}
		<p class="text-xs text-hot">{error}</p>
	{/if}
</div>
