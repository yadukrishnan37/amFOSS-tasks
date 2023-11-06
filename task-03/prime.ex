defmodule Prime do
    def is_prime(n) do
      l = Enum.reduce(1..(n + 1), 0, fn i, l ->
        if rem(n, i) == 0, do: l + 1, else: l
      end)

      if l == 2 do
        1
      else
        0
      end
    end

    def printer do
      IO.puts("Enter the limit: ")
      n = IO.gets("") |> String.trim() |> String.to_integer()

      for i <- 2..(n + 1) do
        if is_prime(i) == 1 do
          IO.write(i)
          IO.write(" ")
        end
      end
      IO.puts("")
    end
  end

  Prime.printer()
