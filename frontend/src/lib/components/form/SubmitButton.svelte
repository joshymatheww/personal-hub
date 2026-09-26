<script lang="ts">
	import type { HTMLButtonAttributes } from 'svelte/elements';

	type Props = {
		title: string;
		disabled?: boolean;
	} & HTMLButtonAttributes;

	let { title, disabled = false, ...restPorps }: Props = $props();
</script>

<button
	class="w-full rounded-md bg-ink px-4 py-2.5 font-medium text-panel hover:bg-ink/90"
	{...restPorps}
	{disabled}
>
	{title}
</button>
