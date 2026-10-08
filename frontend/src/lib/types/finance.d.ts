export type AccountTypes = string[];
export type PaymentModes = string[];
export type TransactionTypes = string[];
export interface Categories {
	income: string[];
	expense: string[];
	transfer: string[];
}

export interface FinanceMeataData {
	account_types: AccountTypes;
	payment_modes: PaymentModes;
	transaction_types: TransactionTypes;
	categories: Categories;
}

export interface AccountBase {
	name: string;
	type: string;
	balance: number;
}

export interface Account extends AccountBase {
	id: number;
}

export interface AccountUpdate {
	name?: string;
	type?: string;
	balance?: number;
}

export interface TransactionGroupBase {
	name: string;
	description?: string;
}

export interface TransactionGroup extends TransactionGroupBase {
	id: number;
}

export interface TransactionGroupUpdate {
	name?: string;
	description?: string;
}
