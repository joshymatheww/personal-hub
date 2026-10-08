import { updateResource } from '$lib/apis/http';
import type { TransactionGroup, TransactionGroupUpdate } from '$lib/types/finance';
import { BaseForm } from '$lib/models/base-form.svelte';

export class TransactionGroupUpdateForm extends BaseForm<TransactionGroupUpdate, TransactionGroup> {
	name = $state('');
	description = $state('');
	id = $state(0);

	constructor(group: TransactionGroup) {
		super();
		this.name = group.name;
		this.description = group.description ?? '';
		this.id = group.id;
	}

	async executeSubmit(token: string): Promise<TransactionGroup> {
		const updateData: TransactionGroupUpdate = {
			name: this.name,
			description: this.description
		};
		const result = await updateResource<TransactionGroupUpdate, TransactionGroup>(
			updateData,
			token,
			`finance/transaction-group/${this.id}`
		);
		return result;
	}
}
