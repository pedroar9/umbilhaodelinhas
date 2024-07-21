import polars as pl

def create_polars_df():
    pl.Config.set_streaming_chunk_size(4000000)
    
    # Leia um pedaço do arquivo para verificar as colunas
    preview_df = pl.read_csv("data/measurements.txt", separator=";", has_header=False)
    print(preview_df.head())
    
    return (
        pl.scan_csv(
            "data/measurements.txt",
            separator=";",
            has_header=False,
            new_columns=["station", "measure"],
            schema={"station": pl.Utf8, "measure": pl.Float64}
        )
        .group_by("station")
        .agg(
            max=pl.col("measure").max(),
            min=pl.col("measure").min(),
            mean=pl.col("measure").mean()
        )
        .sort("station")
        .collect(streaming=True)
    )

if __name__ == "__main__":
    import time

    start_time = time.time()
    df = create_polars_df()
    took = time.time() - start_time
    print(df)
    print(f"Polars processou em: {took:.2f} sec")
