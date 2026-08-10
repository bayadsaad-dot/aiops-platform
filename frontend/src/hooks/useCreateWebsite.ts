import { useState } from "react";
import {
  createWebsite,
} from "../services/websiteService";
import type {
  WebsiteCreate,
} from "../types/website";

export function useCreateWebsite(
  onSuccess?: () => void
) {
  const [loading, setLoading] = useState(false);

  const create = async (
    website: WebsiteCreate
  ) => {
    setLoading(true);

    try {
      await createWebsite(website);

      onSuccess?.();

      return true;
    } catch (error) {
      console.error(error);
      return false;
    } finally {
      setLoading(false);
    }
  };

  return {
    create,
    loading,
  };
}