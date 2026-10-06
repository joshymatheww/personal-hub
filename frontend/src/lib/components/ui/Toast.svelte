<script lang="ts">
	import type { IToast } from '$lib/types/general';
	import Close from '../icons/Close.svelte';

	interface Props {
		toast: IToast;
	}

	let { toast }: Props = $props();
</script>

<div
	class="relative flex h-16 w-60 flex-col justify-center rounded-md border border-line bg-white p-2 shadow-md"
	class:success_toast={toast.type === 'success'}
	class:error_toast={toast.type === 'error'}
>
	<span class="text-sm font-medium">{toast.title}</span>
	<span class="text-xs">{toast.content}</span>
	<button class="absolute top-2 right-2 size-5">
		<span class="sr-only">Close toast</span>
		<Close />
	</button>
</div>
