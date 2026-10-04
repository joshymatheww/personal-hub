<script lang="ts">
	import type { Component } from 'svelte';
	import type { HTMLButtonAttributes } from 'svelte/elements';

	type Props = {
		title: string;
		disabled?: boolean;
		children?: Component;
	} & HTMLButtonAttributes;

	let { title, disabled = false, children, ...restPorps }: Props = $props();
</script>

<button
	class="flex w-full items-center justify-center gap-2 rounded-md bg-ink px-4 py-2.5 font-medium text-panel hover:bg-ink/90"
	{...restPorps}
	{disabled}
>
	{@render children?.()}
	{title}
</button>
