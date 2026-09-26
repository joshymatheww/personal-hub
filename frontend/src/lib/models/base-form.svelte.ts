/**
 * T is for Form Fields, TResponse is for API success object
 */
export abstract class BaseForm<T extends Record<string, any>, TResponse> {
	errors = $state<Partial<Record<keyof T | 'general', string>>>({});
	isSubmitting = $state(false);

	/**
	 * Abstract submission logic implemented by the children classes
	 * Enforces that the child class method returns the exact TResponse
	 */
	abstract executeSubmit(): Promise<TResponse>;

	/**
	 * Main submission handler attached to the <form onsbumit={...}
	 */
	async submit(e: SubmitEvent): Promise<TResponse | null> {
		e.preventDefault();
		this.errors = {};
		this.isSubmitting = true;

		try {
			const data = await this.executeSubmit();
			return data;
		} catch (error) {
			this.handleError(error);
			return null;
		} finally {
			this.isSubmitting = false;
		}
	}

	/**
	 * Standardized FastAPI validation errors mapping
	 */
	private handleError(err: any) {
		if (err.status === 422 && Array.isArray(err.errors)) {
			const newErrors: typeof this.errors = {};
			err.errors.forEach((detail: { loc: (string | number)[]; msg: string }) => {
				const field = detail.loc[detail.loc.length - 1] as keyof T;
				newErrors[field] = detail.msg;
			});
			this.errors = newErrors;
		} else {
			this.errors.general =
				typeof err.errors === 'string' ? err.errors : 'An unexpected error occured';
		}
	}

	/**
	 * Uttility to clear target error fields when a user resumes typing
	 */
	clearError(field: keyof T) {
		if (this.errors[field]) {
			this.errors[field] = undefined;
		}
	}
}
