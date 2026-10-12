<script lang="ts">
	import type { Snippet } from 'svelte';
	import type { HTMLSelectAttributes } from 'svelte/elements';

	type Props = {
		id: string;
		name: string;
		label: string;
		value: string | number;
		placeholder: string;
		error?: string;
		classes?: string;
		children: Snippet;
	} & HTMLSelectAttributes;

	let {
		id,
		name,
		label,
		value = $bindable(),
		placeholder,
		error = '',
		classes = '',
		children,
		...restProps
	}: Props = $props();
</script>

<div class={classes}>
	<label for={id} class="block font-medium">{label}</label>
	<select
		{id}
		{name}
		bind:value
		class="placeholder:text-muted/60 w-full rounded-md border bg-page px-3.5 py-2.5 transition-colors
           {error ? 'border-hot focus:ring-hot' : 'border-line focus:ring-0'}"
	>
		<option value="">{placeholder}</option>
		{@render children()}
	</select>
	{#if error}
		<p class="text-xs text-hot">{error}</p>
	{/if}
</div>
