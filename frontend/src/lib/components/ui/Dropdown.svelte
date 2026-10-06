<script lang="ts">
	import type { Snippet } from 'svelte';
	import { computePosition, offset, flip, shift, autoUpdate } from '@floating-ui/dom';

	interface Props {
		trigger: Snippet;
		children: Snippet;
	}

	let { children, trigger }: Props = $props();
	let isOpen = $state(false);

	let triggerEl: HTMLElement | undefined = $state();
	let contentEl: HTMLElement | undefined = $state();

	function toggleDropdown(e: MouseEvent) {
		e.stopPropagation(); // Stop click from immediately bubbling to window
		isOpen = !isOpen;
	}

	function closeDropdown() {
		isOpen = false;
	}

	// Handle Escape key to close for accessibility
	function handleKeyDown(e: KeyboardEvent) {
		if (e.key === 'Escape') {
			closeDropdown();
		}
	}

	$effect(() => {
		if (isOpen && triggerEl && contentEl) {
			const cleanup = autoUpdate(triggerEl, contentEl, () => {
				if (!triggerEl || !contentEl) return;

				computePosition(triggerEl, contentEl, {
					placement: 'bottom-end',
					strategy: 'fixed', // Explicitly forces calculation relative to viewport
					middleware: [
						offset(8),
						flip({ fallbackAxisSideDirection: 'start' }), // Smarter flipping behavior
						shift({ padding: 8 })
					]
				}).then(({ x, y }) => {
					if (contentEl) {
						Object.assign(contentEl.style, {
							left: `${x}px`,
							top: `${y}px`
						});
					}
				});
			});

			return () => {
				cleanup();
			};
		}
	});
</script>

<!-- Global window listeners manage closing accurately during scrolls and outer clicks -->
<svelte:window onclick={closeDropdown} onkeydown={handleKeyDown} />

<div class="relative inline-block text-left">
	<button
		bind:this={triggerEl}
		onclick={toggleDropdown}
		tabindex="0"
		type="button"
		class="cursor-pointer"
	>
		{@render trigger()}
	</button>

	{#if isOpen}
		<!-- stopPropagation prevents menu body clicks from hitting the window listener -->
		<!-- svelte-ignore a11y_no_static_element_interactions -->
		<!-- svelte-ignore a11y_click_events_have_key_events -->
		<div
			bind:this={contentEl}
			onclick={(e) => e.stopPropagation()}
			class="fixed top-0 left-0 z-50 w-56 rounded-md bg-white p-1 shadow-lg ring-1 ring-black/5 focus:outline-hidden dark:bg-zinc-900 dark:ring-white/10"
		>
			{@render children()}
		</div>
	{/if}
</div>
