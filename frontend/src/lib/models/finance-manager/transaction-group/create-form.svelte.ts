import { postResource } from '$lib/apis/http';
import type { TransactionGroupBase, TransactionGroup } from '$lib/types/finance';
import { BaseForm } from '$lib/models/base-form.svelte';

export class TransactionGroupForm extends BaseForm<TransactionGroupBase, TransactionGroup> {
	name = $state('');
	description = $state('');

	async executeSubmit(token: string): Promise<TransactionGroup> {
		const newGroup: TransactionGroupBase = {
			name: this.name,
			description: this.description
		};
		const result = await postResource<TransactionGroupBase, TransactionGroup>(
			newGroup,
			token,
			'finance/transaction-group'
		);
		return result;
	}

	resetForm() {
		this.name = '';
		this.description = '';
	}
}
