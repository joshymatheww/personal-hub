<script lang="ts">
	import type { Snippet } from 'svelte';

	interface Props {
		trigger: Snippet;
		children: Snippet;
	}

	let { children, trigger }: Props = $props();
	let isOpen = $state(false);

	function toggleDropdown() {
		isOpen = !isOpen;
	}

	function handleFocusOut(e: FocusEvent) {
		if (
			e.relatedTarget &&
			e.currentTarget instanceof HTMLElement &&
			e.currentTarget.contains(e.relatedTarget as Node)
		) {
			return;
		}
		isOpen = false;
	}
</script>

<div class="relative inline-block text-left" onfocusout={handleFocusOut}>
	<div onclick={toggleDropdown} role="button" tabindex="0">
		{@render trigger()}
	</div>
	{#if isOpen}
		<div
			class="absolute right-0 z-50 mt-2 w-56 origin-top-right rounded-md bg-white p-1 shadow-lg ring-1 ring-black/5 focus:outline-hidden dark:bg-zinc-900 dark:ring-white/10"
		>
			{@render children()}
		</div>
	{/if}
</div>
