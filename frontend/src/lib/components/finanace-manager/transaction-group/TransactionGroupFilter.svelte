<script lang="ts">
	interface Props {
		filterBy: {
			name: string;
		};
	}

	let { filterBy = $bindable() }: Props = $props();
</script>

<div class="mb-4 flex flex-wrap items-center gap-3 rounded-lg border border-line bg-panel p-4">
	<label class="relative min-w-50 flex-1">
		<svg
			viewBox="0 0 24 24"
			class="text-muted pointer-events-none absolute top-1/2 left-3 h-4 w-4 -translate-y-1/2"
			fill="none"
			stroke="currentColor"
			stroke-width="1.8"><circle cx="11" cy="11" r="6" /><path d="M20 20l-3.5-3.5" /></svg
		>
		<input
			id="account_name"
			type="search"
			placeholder="Search transaction group"
			class="w-full rounded-md border border-line bg-page py-2 pr-3 pl-9 text-sm focus:ring-0"
			bind:value={filterBy.name}
		/>
	</label>
</div>
