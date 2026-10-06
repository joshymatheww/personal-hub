<script lang="ts">
	import type { Snippet } from 'svelte';
	import { fade, scale } from 'svelte/transition';
	import Close from '../icons/Close.svelte';

	interface Props {
		isOpen: boolean;
		title?: string;
		children: Snippet;
		footer?: Snippet;
	}

	let { isOpen = $bindable(), title, children, footer }: Props = $props();
	let dialogEl: HTMLDialogElement | undefined = $state();

	function handleClose() {
		isOpen = false;
	}

	function handleBackdropClick(e: MouseEvent) {
		if (e.target === dialogEl) {
			handleClose();
		}
	}

	$effect(() => {
		if (isOpen) {
			dialogEl?.showModal();
			document.body.style.overflow = 'hidden';
		} else {
			dialogEl?.close();
			document.body.style.overflow = '';
		}
	});
</script>

{#if isOpen}
	<dialog
		bind:this={dialogEl}
		onclose={handleClose}
		onclick={handleBackdropClick}
		transition:fade={{ duration: 150 }}
		class="max-h-(screen-16) fixed inset-0 z-50 m-auto flex w-full max-w-lg flex-col overflow-hidden rounded-xl border border-line bg-panel p-0 font-sans text-ink shadow-2xl outline-hidden backdrop:bg-black/40 backdrop:backdrop-blur-xs"
	>
		<div
			transition:scale={{ start: 0.95, duration: 150 }}
			class="flex w-full flex-col overflow-hidden"
		>
			<!-- Modal Header Section -->
			<div class="flex items-center justify-between border-b border-line px-6 py-4">
				{#if title}
					<h3 class="font-display text-lg font-semibold tracking-tight text-ink">
						{title}
					</h3>
				{:else}
					<div></div>
				{/if}
				<button
					type="button"
					onclick={handleClose}
					class="text-muted cursor-pointer rounded-md p-1.5 hover:bg-page hover:text-ink focus-visible:outline-2 focus-visible:outline-ink"
					aria-label="Close modal"
				>
					<Close />
				</button>
			</div>

			<!-- Scrollable Modal Content Body -->
			<div class="overflow-y-auto px-6 py-4 text-sm leading-relaxed text-ink/90">
				{@render children()}
			</div>

			<!-- Optional Footer Actions Slot -->
			{#if footer}
				<div
					class="flex items-center justify-end gap-3 border-t border-line bg-page/30 px-6 py-3.5"
				>
					{@render footer()}
				</div>
			{/if}
		</div>
	</dialog>
{/if}
